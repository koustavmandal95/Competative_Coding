class BirdCount
{
    private int[] birdsPerDay;

    public BirdCount(int[] birdsPerDay)
    {
        this.birdsPerDay = birdsPerDay;
    }

    public static int[] LastWeek()
    {
        int [] lastWeek = new int [] {0,2,5,3,7,8,4};
        return lastWeek;
    }

    public int Today()
    {
        return birdsPerDay[birdsPerDay.Length-1];
    }

    public void IncrementTodaysCount()
    {
         birdsPerDay[birdsPerDay.Length-1] = birdsPerDay[birdsPerDay.Length-1] + 1;
    }

    public bool HasDayWithoutBirds()
    {
       foreach(int birdsVisited in birdsPerDay)
        {
            if (birdsVisited == 0)
                return true;
        }
        return false;
    }

    public int CountForFirstDays(int numberOfDays)
    {
        int sumTotal = 0;
        for(int i=0; i < numberOfDays;i++)
        {
            sumTotal += birdsPerDay[i];
        }
        return sumTotal;
    }

    public int BusyDays()
    {
        int countNumberOfBusyDays = 0;
        foreach(int birdsVisited in birdsPerDay)
        {
            if (birdsVisited >=5)
                countNumberOfBusyDays += 1;
        }
        return countNumberOfBusyDays ;
    }
}
