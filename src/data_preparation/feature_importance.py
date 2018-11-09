import pandas as pd
import numpy as np
import scipy.stats as stats
from scipy.stats import chi2_contingency



class ChiSquare:
    def __init__(self, dataframe):
        self.df = dataframe
        self.p = None #P-Value
        self.chi2 = None #Chi Test Statistic
        self.dof = None

        self.dfObserved = None
        self.dfExpected = None
    def _print_chisquare_result(self, colX, alpha):
        result = ""
        if self.p<alpha:
            result="{0} IMPORTANT".format(colX)
        else:
            result="{0} NOT_IMPORTANT".format(colX)

        print(result)

    def TestIndependence(self,colX,colY, alpha=0.05):
        X = self.df[colX].astype(str)
        Y = self.df[colY].astype(str)

        self.dfObserved = pd.crosstab(Y,X)
        chi2, p, dof, expected = stats.chi2_contingency(self.dfObserved.values)
        self.p = p
        self.chi2 = chi2
        self.dof = dof

        self.dfExpected = pd.DataFrame(expected, columns=self.dfObserved.columns, index = self.dfObserved.index)

        self._print_chisquare_result(colX,alpha)
if __name__ == "__main__":
    df = pd.read_csv('/Users/apple/Desktop/final_lasvegas_dataset.csv')
    # df['dummyCat'] = np.random.choice([0, 1], size=(len(df),), p=[0.5, 0.5])
    df.head()
    cT = ChiSquare(df)
    #Feature Selection
    testColumns = ['name','location_name','category_name','address','city','state','zip_code','violations','current_demerits','inspection_demerits','neighborhood','rating','review_count','accepts_insurance','ages_allowed','alcohol','ambience','byob','byob_corkage','best_nights','bike_parking','business_accepts_bitcoin','business_accepts_creditcards','business_parking','byappointmentonly','caters','coat_check','corkage','dietary_restrictions','dogs_allowed','drive_thru','good_for_dancing','good_for_kids','good_for_meal','hair_specializes_in','happy_hour','has_tv','music','noise_level','open_24_hours','outdoor_seating','restaurants_attire','restaurants_counter_service','restaurants_delivery','restaurants_good_for_groups','restaurants_price_range2','restaurants_reservations','restaurants_table_service','restaurants_takeout','smoking','wheelchair_accessible','wifi']
    for var in testColumns:
        cT.TestIndependence(colX=var,colY="inspection_grade" )
