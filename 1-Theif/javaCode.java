package theif;

import java.util.Scanner;

public class Theif {

    public static void main(String[] args) {
        // TODO code application logic here
        Scanner sc = new Scanner(System.in);
        byte[] numbers = new byte[4];
        
        for(byte i = 0; i < 4; i++){
            System.out.println("please input the "+(i+1)+"th digit");
            numbers[i] = sc.nextByte();
        }
        for(byte i = 0; i < 4; i++){
            byte digit1 = numbers[i];
            //IOHandler.print(digit1);
            for(byte j = 0; j < 4; j++){
                if(i!=j){
                    byte digit2 =  numbers[j];
                    for(byte k = 0; k < 4; k++){
                        if(i!=k && j!=k){
                            byte digit3 =  numbers[k];
                            for(byte l = 0; l < 4; l++){
                                if(i!=l && j!=l && k!=l){
                                    byte digit4 =  numbers[l];
                                    System.out.print(digit1);
                                    System.out.print(digit2);
                                    System.out.print(digit3);
                                    System.out.println(digit4);
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
