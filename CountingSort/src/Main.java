import java.util.Scanner;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int[] arr=new int[n];
        int[] result=new int[n];
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }
        int k=Arrays.stream(arr).max().getAsInt();
        int[] count=new int[k+1];
        for(int i=0;i<=k;i++){
            count[i]=0;
        }
        for(int i=0;i<n;i++){
            count[arr[i]]++;
        }
        for(int i=1;i<=k;i++){
            count[i]+=count[i-1];
        }
        for(int i=n-1;i>=0;i--){
            result[count[arr[i]]-1]=arr[i];
            count[arr[i]]--;
        }
        for(int i=0;i<n;i++) System.out.print(result[i]+" ");
    }
}