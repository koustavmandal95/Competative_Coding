public static class SumOfMultiples
{
    public static int Sum(IEnumerable<int> multiples, int max)
    {
        HashSet<int> multipleSet = new HashSet<int>();
        foreach(int multiple in multiples)
        {
            if (multiple <=0)
                break;
            int number = multiple;
            while(number < max)
            {
                multipleSet.Add(number);
                number += multiple;
            }
        }
        return multipleSet.Sum();                    
    }
}