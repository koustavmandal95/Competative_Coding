public static class ResistorColorDuo
{
    public static int Value(string[] colors)
    {
        string [] ColorCode = new string [] {"black","brown","red","orange","yellow","green","blue","violet","grey","white"};       
        
        int firstband = Array.IndexOf(ColorCode,colors[0]);
        int secondband = Array.IndexOf(ColorCode,colors[1]);
        int finalValue = firstband*10+secondband;
        return finalValue;
    }
}
