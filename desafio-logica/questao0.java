package org.example;

import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class questao0 {
    public static void main(String[] args) {
        //desafio 0 questão 1;
        System.out.print("Informe o tamanho do array: ");
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        List<Integer> a = new LinkedList<>();
        for (int i=1;i<=n;i++){
            a.add(i);
        }
        for (int i=0;i<n;i+=2){
            System.out.print(a.get(i) +" ");
        }

        //desafio 0 questão 2;
        System.out.println("\nInforme o indice do número na sequencia de fibonacci");
        n = scanner.nextInt();
        int fibonacci=Fibonacci.fibo(n);
        String fibonacciString = Integer.toString((int) fibonacci);
        if(fibonacciString.length()>2){
            fibonacciString=fibonacciString.substring(fibonacciString.length()-2);
        }
        System.out.println(fibonacci);
        System.out.println(fibonacciString);
    }
}

class Fibonacci {

    static int fibo(int n) {
        if (n < 2) {
            return n;
        } else {
            return fibo(n - 1) + fibo(n - 2);
        }
    }
}