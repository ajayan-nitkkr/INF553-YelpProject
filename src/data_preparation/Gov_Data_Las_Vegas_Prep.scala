import java.io.File

import org.apache.hadoop.fs.FileUtil
import org.apache.spark.{SparkConf, SparkContext}
import org.apache.hadoop.conf.Configuration
import org.apache.hadoop.fs._
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._

/**Ø
  * Created by lnahoom on 22/08/2016.
  */
object Gov_Data_Las_Vegas_Prep {

  def main(args: Array[String]): Unit = {
    //replace x with args(0)
    val inputPath = "/Users/apple/Documents/DM/Project/las_vegas/Restaurant_Inspections_LV.csv"

    //replace y with args(1)
    val outputPath = "/Users/apple/Documents/DM/Project/las_vegas/Restaurant_Inspections_LV_Final.csv"

    val conf = new SparkConf()
    conf.setAppName("Datasets Test")
    conf.setMaster("local[2]")
    val spark_context = new SparkContext(conf)
    val sparkSession = SparkSession
      .builder()
      .config(conf)
      .getOrCreate()

    val dfTags = sparkSession
      .read
      .option("header", "true")
      .option("inferSchema", "false")
      .csv(inputPath)
      .toDF()

    val myCols = dfTags.select("Restaurant Name","Location Name" ,"Category Name", "Address",	"City",	"State",	"Zip",	"Current Demerits","Current Grade",
      "Inspection Date","Inspection Demerits","Inspection Grade","Permit Status","Inspection Result","Violations","Date Current")

    //count number of violations
    val newDf = myCols.columns.foldLeft(myCols)((curr, n) => curr.withColumnRenamed(n, n.replaceAll("\\s", "")))
    def range = udf((violations: String) => {
      violations.split(",").length
    })
    val violationsCount = newDf.withColumn("ViolationsCount",range(col("Violations")))

    //replace zip with only first five digits
    //replace zip with only first five digits
    def zipFormat = udf((zip: String) => {
      val lastindex = zip.indexOf('-')
      var result = zip
      if(lastindex != -1) result = zip.substring(0,lastindex)
      result
    })
    val zipFormatted = violationsCount.withColumn("ZipCode",zipFormat(col("Zip"))).drop("Zip").withColumnRenamed("ZipCode","Zip")
    zipFormatted.take(4).foreach(println)

    def addScoreFromGrade = udf((grade: String) => {
      var score = 0
      if (grade == "A") score = 95
      else if (grade == "B") score = 85
      else if (grade == "C") score = 75
      else if (grade == "N") score = 35
      else if (grade == "O") score = 35
      else if (grade == "X") score = 65
      else if (grade == "P") score = 35
      else if (grade == "S") score = 35
      score
    })
    val scoresFromGradesCurrent = zipFormatted.withColumn("CurrentScore",addScoreFromGrade(col("CurrentGrade")))


    val scoresFromGradesInspection = scoresFromGradesCurrent.withColumn("InspectionScore",addScoreFromGrade(col("InspectionGrade")))

    val uniqueDf = scoresFromGradesInspection.groupBy("RestaurantName",	"LocationName",	"CategoryName",	"Address","City","State","Zip")
      .agg(sum("ViolationsCount") as "Violations",sum("CurrentDemerits") as "CurrentDemerits",
        sum("InspectionDemerits") as "InspectionDemerits",avg("CurrentScore")
          as "CurrentScore",avg("InspectionScore") as "InspectionScore"
      )

    def addGradeFromScore = udf((score_number: String) => {
      val score = score_number.toDouble
      var grade = ""
      if (score >= 90) grade = "A"
      else if (score >= 80 && score < 90) grade = "B"
      else if (score >= 70 && score < 80) grade = "C"
      else if (score >= 60 && score < 70) grade = "D"
      else if (score >0 && score <60) grade = "E"
      grade
    })
    val finalDf1 = uniqueDf.withColumn("CurrentGrade",addGradeFromScore(col("CurrentScore")))
    val finalDf2 = finalDf1.withColumn("InspectionGrade",addGradeFromScore(col("InspectionScore")))

    val file = outputPath.substring(0,outputPath.lastIndexOf('/'))+"/temp.csv"
    FileUtil.fullyDelete(new File(file))
    val destinationFile = outputPath
    FileUtil.fullyDelete(new File(destinationFile))

    finalDf2.coalesce(1).write.option("header", "true").csv(file)
    merge(file, destinationFile)

    val currentGradeCount =  finalDf2.groupBy("CurrentGrade").count().show();
    val inspectionGradeCount =  finalDf2.groupBy("InspectionGrade").count().show();
  }

  def merge(srcPath: String, dstPath: String): Unit =  {
    val hadoopConfig = new Configuration()
    val hdfs = FileSystem.get(hadoopConfig)
    FileUtil.copyMerge(hdfs, new Path(srcPath), hdfs, new Path(dstPath), true, hadoopConfig, null)
  }
}
