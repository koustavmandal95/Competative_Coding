public static class DifferenceOfSquares
{
    public static int CalculateSquareOfSum(int max)
    {
        int sumAll = (max)*(max+1)/2;
        return sumAll*sumAll; 
    }

    public static int CalculateSumOfSquares(int max)
    {
        int calculateAll = (max*(max+1)*(2*max+1))/6;
        return calculateAll;   
    }
    
    public static int CalculateDifferenceOfSquares(int max)
    {
        return CalculateSquareOfSum(max) - CalculateSumOfSquares(max);
    }
}