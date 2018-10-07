import java.io.IOException;
import java.security.KeyManagementException;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.security.cert.CertificateException;
import java.security.cert.X509Certificate;

import javax.net.ssl.HostnameVerifier;
import javax.net.ssl.HttpsURLConnection;
import javax.net.ssl.SSLContext;
import javax.net.ssl.SSLSession;
import javax.net.ssl.X509TrustManager;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;

public class InspectionCrawler {

	private static String input_weblink = "https://ehservices.publichealth.lacounty.gov/ezsearch"; 
	
	/**
	 * This implementation has been copied from Internet
	 * Reference link: "https://nanashi07.blogspot.com/2014/06/enable-ssl-connection-for-jsoup.html"
	 * @throws KeyManagementException
	 * @throws NoSuchAlgorithmException
	 */
    public static void enableSSLSocket() throws KeyManagementException, NoSuchAlgorithmException {
        HttpsURLConnection.setDefaultHostnameVerifier(new HostnameVerifier() {
            public boolean verify(String hostname, SSLSession session) {
                return true;
            }
        });
 
        SSLContext context = SSLContext.getInstance("TLS");
        context.init(null, new X509TrustManager[]{new X509TrustManager() {
            public void checkClientTrusted(X509Certificate[] chain, String authType) throws CertificateException {
            }
 
            public void checkServerTrusted(X509Certificate[] chain, String authType) throws CertificateException {
            }
 
            public X509Certificate[] getAcceptedIssuers() {
                return new X509Certificate[0];
            }
        }}, new SecureRandom());
        HttpsURLConnection.setDefaultSSLSocketFactory(context.getSocketFactory());
    }
 
    public static void scrap_html() {
		Document doc = null;
		try {
			
			/**
			 * Issue resolved - How to connect to link
			 * Reference Link: "https://github.com/jhy/jsoup/issues/680"
			 */
			enableSSLSocket();
			doc = Jsoup.connect(input_weblink).get();
		} catch (IOException e) {
			System.out.println("Error: IOException");
			e.printStackTrace();
		} catch (KeyManagementException e) {
			System.out.println("Error: KeyManagementException");
			e.printStackTrace();
		} catch (NoSuchAlgorithmException e) {
			System.out.println("Error: NoSuchAlgorithmException");
			e.printStackTrace();
		}
		if (doc == null) {
			return;
		}
		System.out.println(doc.title());
    }
    
	public static void main(String[] args) {
		scrap_html();
	}
}
