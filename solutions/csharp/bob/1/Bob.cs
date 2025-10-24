public static class Bob
{
    public static string Response(string statement)
    {
        if(statement.Where(char.IsLetter).All(char.IsUpper) && statement.Any(char.IsLetter) &&statement.Contains("?"))
        {
            return "Calm down, I know what I'm doing!";         
        }
        else if((statement.EndsWith('?') || statement.EndsWith("?   ")))
        {
          return "Sure.";
        }
        else if((string.IsNullOrWhiteSpace(statement) || string.IsNullOrEmpty(statement)))
        {
            return "Fine. Be that way!";   
        }        
        else if(statement.Where(char.IsLetter).All(char.IsUpper) && statement.Any(char.IsLetter))
        {
            return "Whoa, chill out!";    
        }
        return "Whatever.";
    }
}