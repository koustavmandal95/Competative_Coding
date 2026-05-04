public static class LineUp
{
    public static string Format(string name, int number)
    {
        string suffix = GetSuffix(number);
        return FormatMessage(name, number, suffix);
    }

    private static string GetSuffix(int number)
    {
        int lastTwoDigits = number % 100;
        int lastDigit = number % 10;

        if (lastTwoDigits is 11 or 12 or 13)
            return "th";

        return lastDigit switch
        {
            1 => "st",
            2 => "nd",
            3 => "rd",
            _ => "th"
        };
    }

    private static string FormatMessage(string name, int number, string suffix) 
        => $"{name}, you are the {number}{suffix} customer we serve today. Thank you!";

}
