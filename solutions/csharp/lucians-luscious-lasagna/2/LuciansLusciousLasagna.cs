class Lasagna
{
    private const int ExpectedTimeInOven = 40;
    private const int preparationTimePerLayer = 2;
    
    public int ExpectedMinutesInOven() => ExpectedTimeInOven;

    public int RemainingMinutesInOven(int timeInOven) => ExpectedMinutesInOven() - timeInOven;

    public int PreparationTimeInMinutes(int numberOfLayers) => numberOfLayers*preparationTimePerLayer;

    public int ElapsedTimeInMinutes(int numberOfLayers, int timeInOven) => PreparationTimeInMinutes(numberOfLayers) + timeInOven;
    

}
