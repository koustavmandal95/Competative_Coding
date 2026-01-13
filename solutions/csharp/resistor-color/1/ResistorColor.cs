public static class ResistorColor
{
    public static int ColorCode(string color)
    {
        return Array.IndexOf(ResistorColor.Colors(),color);
    }

    public static string[] Colors()
    {
         string [] colors = new string [] { "black" , "brown", "red", "orange", "yellow" , "green" , "blue", "violet", "grey",                                                  "white" };
        return colors;
    }
}