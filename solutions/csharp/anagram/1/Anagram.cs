using System.Linq;
public class Anagram
{
    public string BaseWord {get;set;}

    public List<string> finalAnagramList = new List<string>();
    
    public Anagram(string baseWord)
    {
        BaseWord = baseWord;
    }

    public string[] FindAnagrams(string[] potentialMatches)
    {
        
        foreach(string candidate in potentialMatches)
        {
            List<char> anagram = BaseWord.ToLower().ToList();
            List<char> temperoryWord = candidate.ToLower().ToList();
            
            if(String.Equals(candidate,BaseWord ,StringComparison.OrdinalIgnoreCase) ||
               BaseWord.Length != candidate.Length)
                continue;
            
            foreach(char character in temperoryWord)
            {
                if(anagram.Contains(character))
                {
                    anagram.Remove(character);
                }
            }
            if(anagram.Count == 0)
            {
                Console.WriteLine(candidate);
                finalAnagramList.Add(candidate);
            }    
        }
        return finalAnagramList.ToArray();
    }
}