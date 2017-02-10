package org.usfirst.frc.team5426.client;

import java.io.*;
import java.net.Socket;

public class Client {

    public Client(String host, int port) {

        try {
            
            Socket socket = new Socket(host, port);
            

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {

        new Client("127.0.0.1", 5426);
    }
}
