package com.example.myapplication;

import android.media.MediaPlayer;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.os.Environment;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowCompat;
import androidx.core.view.WindowInsetsCompat;

import java.io.File;
import java.io.IOException;

public class MainActivity extends AppCompatActivity {
    private MediaPlayer mediaPlayer;
    private int current = 0;
    private File currsong = null;
    @Override
    protected void onCreate(Bundle savedInstanceState) {super.onCreate(savedInstanceState);
        File datadir = new File(Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_MUSIC), "musiclist");
        if(!datadir.exists()){
            boolean ok = datadir.mkdir();
        }
        WindowCompat.enableEdgeToEdge(getWindow());
        setContentView(R.layout.activity_main);
        final EditText edittext = findViewById(R.id.editTextText);
        Button button = findViewById(R.id.button);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String input = edittext.getText().toString();
                File listname = new File(datadir,input);

                choocecurr(listname);
            }
        });
    }
    private void choocecurr(File listname){
        current++;
        boolean found = false;
        File[] songs = listname.listFiles();
        if(songs != null) {
            for (File file : songs) {
                if (file.getName().startsWith("---" + current + "-") ) {
                    currsong = file;
                    found = true;
                    break;
                }
            }
        }
        if(found){
            play(listname);
        }
    }
    private void play(File listname){
        if (mediaPlayer != null) {
            mediaPlayer.release();
            mediaPlayer = null;
        }
        try {
            mediaPlayer = new MediaPlayer();
            mediaPlayer.setDataSource(currsong.getAbsolutePath());
            mediaPlayer.prepare();
            mediaPlayer.start();
            mediaPlayer.setOnCompletionListener(mp ->{
                choocecurr(listname);
            });
        }catch (IOException e) {
            e.printStackTrace();
        }
    }
    @Override
    protected void onDestroy() {
        super.onDestroy();
        if (mediaPlayer != null) {
            mediaPlayer.release();
            mediaPlayer = null;
        }
    }
}