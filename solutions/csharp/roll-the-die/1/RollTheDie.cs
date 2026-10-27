public class Player
{
    public Random myRandomNumber = new Random();
    public int RollDie()
    {
        return myRandomNumber.Next(1,19);
    }

    public double GenerateSpellStrength()
    {
        return myRandomNumber.NextDouble()*100.0;
    }
}
