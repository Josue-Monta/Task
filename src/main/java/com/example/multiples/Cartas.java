package com.example.multiples;

import javafx.application.Application;
import javafx.stage.Stage;
import javafx.util.Pair;

import java.util.List;

public class Cartas {
    public static void main(String[] args) {
        List<Pair<String, String>> jugadas = List.of(
                new Pair<>("R", "S"),
                new Pair<>("S", "R"),
                new Pair<>("P", "S")
        );

        String ganador = calcularGanador(jugadas);
        System.out.println("El ganador es: " + ganador);
    }

    public static String calcularGanador(List<Pair<String, String>> jugadas) {
        int ganador1 = 0;
        int ganador2 = 0;

        for (Pair<String, String> jugada : jugadas) {
            String jugador1 = jugada.getKey();
            String jugador2 = jugada.getValue();

            if ((jugador1.equals("R") && jugador2.equals("S")) ||
                    (jugador1.equals("S") && jugador2.equals("P")) ||
                    (jugador1.equals("P") && jugador2.equals("R"))) {
                ganador1++;
            } else if ((jugador1.equals("S") && jugador2.equals("R")) ||
                    (jugador1.equals("P") && jugador2.equals("S")) ||
                    (jugador1.equals("R") && jugador2.equals("P"))) {
                ganador2++;
            }
        }

        if (ganador1 > ganador2) {
            return "Player 1";
        } else if (ganador2 > ganador1) {
            return "Player 2";
        } else {
            return "Tie";
        }
    }
}
