package com.example.multiples;

public class Multiple {
    public static void main(String[] args) {
    System.out.println("Numbers from 1 to 100 ");

    for(int i =1; i<=100; i++){
        if (i%3==0 & i%5==0){
            System.out.println("fizzbuzz");

            } else if (i%3==0) {
            System.out.println("fizz");
            } else if(i%5==0){
            System.out.println("buzz");

            }else {
            System.out.println(i);
            }
        }
    }
}


