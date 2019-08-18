// https://www.codechef.com/problems/CSUB
import java.util.Scanner;
class CSUB
{
	public static void main(String args[])
	{
		Scanner sc= new Scanner(System.in);
		int t,len,ctr=0;
		t=sc.nextInt();
		String str;
		while(t>0)
		{
			len=sc.nextInt();
			str=sc.next();
			for(int i=0;i<len;i++)
			{
				if(str.charAt(i)=='1')
				{
					ctr++;	
				}
			}
			for(int i=0;i<len;i++)
			{
				for(int j=i+1;j<len;j++)
				{
					if(str.charAt(i)=='1' && str.charAt(j)=='1')
					{
						ctr++;
					}	
				}
			}
			System.out.println(ctr);
			t--;
					
		}
		
	}
}