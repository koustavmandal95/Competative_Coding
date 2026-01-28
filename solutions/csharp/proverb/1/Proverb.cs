public static class Proverb
{
    public static string[] Recite(string[] subjects)
    {
        string [] allStrings = new string[subjects.Length];
        for( int i =0; i < subjects.Length-1; i++)
        {
            allStrings[i] = $"For want of a {subjects[i]} the {subjects[i+1]} was lost.";
        }
        if(subjects.Length !=0)
            allStrings[subjects.Length-1] = $"And all for the want of a {subjects[0]}.";

        foreach(var item in allStrings)
        {
            Console.WriteLine(item);
        }
        return allStrings;
    }
}