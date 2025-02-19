import java.util.Scanner;

public class reverse {
    
    // Function to reverse the string
    public static String reverseString(String str) {
        // Convert string to character array
        char[] strArray = str.toCharArray();
        
        // Initialize variables to point to the start and end of the array
        int start = 0;
        int end = strArray.length - 1;
        
        // Swap characters from start and end until they meet in the middle
        while (start < end) {
            // Swap the characters
            char temp = strArray[start];
            strArray[start] = strArray[end];
            strArray[end] = temp;
            
            // Move the pointers towards the center
            start++;
            end--;
        }
        
        // Convert character array back to string and return
        return new String(strArray);
    }

    public static void main(String[] args) {
        // Create scanner object for user input
        Scanner scanner = new Scanner(System.in);
        
        // Ask user to input a string
        System.out.print("Enter a string: ");
        String input = scanner.nextLine();
        
        // Reverse the string
        String reversed = reverseString(input);
        
        // Print the reversed string
        System.out.println("Reversed string: " + reversed);
        
        // Close the scanner
        scanner.close();
    }
}
