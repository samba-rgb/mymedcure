package id.samai.mymedcure.activities;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.webkit.WebView;
import android.webkit.WebViewClient;

import id.samai.mymedcure.R;

public class web_article extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_web_article);
        WebView w = (WebView) findViewById(R.id.web);

        // loading http://www.google.com url in the the WebView.
        w.loadUrl("https://my.clevelandclinic.org/health/articles/4062-chronic-illness");

        // this will enable the javascipt.
        w.getSettings().setJavaScriptEnabled(true);

        // WebViewClient allows you to handle
        // onPageFinished and override Url loading.
        // w.setWebViewClient(new WebViewClient());
        w.setWebViewClient(new WebViewClient() {
            public boolean shouldOverrideUrlLoading (WebView view, String url){
                //True if the host application wants to leave the current WebView and handle the url itself, otherwise return false.
                return true;
            }
        });
    }
}