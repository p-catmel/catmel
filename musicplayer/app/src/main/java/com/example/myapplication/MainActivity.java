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
import java.util.ArrayList;
import java.util.List;
public class MainActivity extends AppCompatActivity {
    private MediaPlayer mediaPlayer;
    private int currindex = 0;
    private List<File> files = new ArrayList<>();
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
                load(listname);
                play();
            }
        });
    }
    private void load(File listname) {
        currindex = 0;
        files.clear();
        boolean found = false;
        int j = 0;
        File[] songs = listname.listFiles();
        if (songs != null) {
            for (int i = 1; j < songs.length; i++){
                for (File file : songs) {
                    if (file.getName().startsWith("---" + i + "-")) {
                        files.add(file);
                        j++;
                        found = true;
                        break;
                    }
                }
            }
        }
    }
    private void play(){
        if (mediaPlayer != null) {
            mediaPlayer.release();
            mediaPlayer = null;
        }
        try {
            if(currindex >= files.size()){
                return;
            }
            File currsong = files.get(currindex);
            mediaPlayer = new MediaPlayer();
            mediaPlayer.setDataSource(currsong.getAbsolutePath());
            mediaPlayer.prepare();
            mediaPlayer.start();
            mediaPlayer.setOnCompletionListener(mp ->{
                currindex++;
                play();
            });
        }catch (IOException e) {
            currindex++;
            play();
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