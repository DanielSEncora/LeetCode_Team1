import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] nums1 = {10,3,5};
        int[] nums2 = {2,9,9};
        System.out.println(findMedianSortedArrays(nums1,nums2));
    }

    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        //Initialized an array with the length of the two original arrays added up.
        int[] newArray = new int[nums1.length + nums2.length];
        //Assigned the nums1 and nums2 values to the newArray by copying them
        System.arraycopy(nums1, 0, newArray, 0,nums1.length);
        System.arraycopy(nums2, 0, newArray, nums1.length,nums2.length);
        //Sorted the array in ascending order.
        Arrays.sort(newArray);

        /*Checks if array.length is an even number. If it is, it returns the value of the 2 middle indexes divided by two.
        If the array.length is an odd number it just return the value in the middle by obtaining the value found in the [array.length/2] index*/
        if(newArray.length%2 == 0){
            return (double) (newArray[newArray.length / 2] + newArray[newArray.length / 2 -1]) / 2;
        }else{
            return newArray[newArray.length/2];
        }
    }
}