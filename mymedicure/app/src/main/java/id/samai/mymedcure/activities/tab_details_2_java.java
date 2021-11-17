package id.samai.mymedcure.activities;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.ncorti.slidetoact.SlideToActView;
import com.squareup.picasso.Picasso;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.Locale;
import java.util.Set;

import id.samai.mymedcure.R;
import id.samai.mymedcure.helpers.DBHelper;
import id.samai.mymedcure.helpers.DataBase2;
import id.samai.mymedcure.models.TABLET;

public class tab_details_2_java extends AppCompatActivity {
    private int id ;
    AlertDialog.Builder builder;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_tab_details_2_java);
        Bundle b = new Bundle();
        builder = new AlertDialog.Builder(this);

        DBHelper dbHelper;
        dbHelper = new DBHelper(getApplicationContext());
        b = getIntent().getExtras();
        String name = b.getString("name");
        String link = b.getString("link");
        String info = b.getString("info");
        String update_info = b.getString("update_info");
        final SlideToActView slide = findViewById(R.id.taken_tik_java);

        TextView name_med = (TextView)findViewById(R.id.medcine_name_java);
        name_med.setText(name);
        TextView info_med = (TextView)findViewById(R.id.info_tab_2_java);
        info_med.setText(info);
        ImageView imageView = findViewById(R.id.image_medicine_java);
        Picasso.get()
                .load(link)
                .error(R.drawable.my_medicure)
                .into(imageView);
        Calendar c = Calendar.getInstance();
        Date date =  new Date();
        c.setTime(date);
        //c.add(Calendar.YEAR, Calendar.YEAR);
        SimpleDateFormat df = new SimpleDateFormat("MMMM dd yyyy (EEE)", Locale.US);
        String  dateTime = df.format(c.getTime()).toString();
        ArrayList<TABLET> schedules = dbHelper.getTabletdatebool(name.toString(), dateTime);
        if(schedules.isEmpty()){
            TABLET sam = new TABLET(id, name.toString(), dateTime, 0, 0, 0, 0);
            dbHelper.insertTABLET_history(sam);
        }
        else {
            TABLET first = schedules.get(0);
            if (update_info.equals("morning")) {
                //Toast.makeText(getApplicationContext(), "morning", Toast.LENGTH_SHORT).show();

                if (first.getMorning() == 1) {
                   // Toast.makeText(getApplicationContext(), "e.getMessage()", Toast.LENGTH_SHORT).show();
                    slide.setVisibility(View.INVISIBLE);
                    builder.setMessage(R.string.dialog_message) .setTitle(R.string.dialog_title);

                    //Setting message manually and performing action on button click
                    builder.setMessage("You have taken this medicine dose")
                            .setCancelable(false)
                            .setPositiveButton("OK", new DialogInterface.OnClickListener() {
                                public void onClick(DialogInterface dialog, int id) {
                                    //do things
                                }
                            });
                    builder.setTitle("Dont take this medicine now");

                    AlertDialog alert = builder.create();

                    alert.show();

        }
            }
            if (update_info.equals("afternoon")) {
                //Toast.makeText(getApplicationContext(), "morning", Toast.LENGTH_SHORT).show();

                if (first.getAfternoon() == 1) {
                    // Toast.makeText(getApplicationContext(), "e.getMessage()", Toast.LENGTH_SHORT).show();
                    slide.setVisibility(View.INVISIBLE);
                    builder.setMessage(R.string.dialog_message) .setTitle(R.string.dialog_title);

                    //Setting message manually and performing action on button click
                    builder.setMessage("You have taken this medicine dose")
                            .setCancelable(false)
                            .setPositiveButton("OK", new DialogInterface.OnClickListener() {
                                public void onClick(DialogInterface dialog, int id) {
                                    //do things
                                }
                            });
                    builder.setTitle("Dont take this medicine now");

                    AlertDialog alert = builder.create();

                    alert.show();

                }
            }
            if (update_info.equals("evening")) {
                //Toast.makeText(getApplicationContext(), "morning", Toast.LENGTH_SHORT).show();

                if (first.getEvening() == 1) {
                    // Toast.makeText(getApplicationContext(), "e.getMessage()", Toast.LENGTH_SHORT).show();
                    slide.setVisibility(View.INVISIBLE);
                    builder.setMessage(R.string.dialog_message) .setTitle(R.string.dialog_title);

                    //Setting message manually and performing action on button click
                    builder.setMessage("You have taken this medicine dose")
                            .setCancelable(false)
                            .setPositiveButton("OK", new DialogInterface.OnClickListener() {
                                public void onClick(DialogInterface dialog, int id) {
                                    //do things
                                }
                            });
                    builder.setTitle("Dont take this medicine now");

                    AlertDialog alert = builder.create();

                    alert.show();

                }
            }
            if (update_info.equals("night")) {
                //Toast.makeText(getApplicationContext(), "morning", Toast.LENGTH_SHORT).show();

                if (first.getNight() == 1) {
                    // Toast.makeText(getApplicationContext(), "e.getMessage()", Toast.LENGTH_SHORT).show();
                    slide.setVisibility(View.INVISIBLE);
                    builder.setMessage(R.string.dialog_message) .setTitle(R.string.dialog_title);

                    //Setting message manually and performing action on button click
                    builder.setMessage("You have taken this medicine dose")
                            .setCancelable(false)
                            .setPositiveButton("OK", new DialogInterface.OnClickListener() {
                                public void onClick(DialogInterface dialog, int id) {
                                    //do things
                                }
                            });
                    builder.setTitle("Dont take this medicine now");

                    AlertDialog alert = builder.create();

                    alert.show();

                }
            }



        }
       // Toast.makeText(getApplicationContext(), "morning_1", Toast.LENGTH_SHORT).show();

        slide.setOnSlideCompleteListener(new SlideToActView.OnSlideCompleteListener() {
            @Override
            public void onSlideComplete(@NonNull SlideToActView view) {
                dbHelper.attend(name,dateTime,update_info);
                dbHelper.degrade(name);
            }
        });







    }

    @Override
    protected void onStart() {

        super.onStart();
    }
}