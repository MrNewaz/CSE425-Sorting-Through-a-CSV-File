
import java. util. Scanner;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class search {

    public static void main(String[] args) {

        File file = new File("heart.csv");

        BufferedReader reader = null;

        String row = null;
        String msg = "Search by Age: 1 \nSearch by Gender :2 \nSearch by CP : 3 \nSearch by trtbps :4 \nSearch by chol : 5 \nSearch by fbs : 6 \nSearch by restecg : 7 \nSearch by thalachh : 8 \nSearch by exng : 9 \nSearch by oldpeak : 10 \nSearch by slp : 11 \nSearch by caa : 12 \nSearch by thall : 13 \nSearch by output : 14 \nExit : 0" ;
        String option= null;
        String keyword= null;
        int n;



        Scanner inn = new Scanner(System.in);
        System.out.println(msg);
        System.out.print("\nOption :");
        option=inn.nextLine();
        System.out.println();
        n=Integer.parseInt(option);


        System.out.print("\nEnter search Element :");


        keyword=inn.nextLine();
        System.out.println("\nResults:\n");
        inn.close();

        try {

            reader = new BufferedReader(new FileReader(file));
            reader.readLine();


            while ((row = reader.readLine()) != null) {

                String[] data = row.split(",");

                if (data[n-1].contains(keyword)) {

                    System.out.println(row);
                }

            }


        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (reader != null) {
                try {
                    reader.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }

    }
}



