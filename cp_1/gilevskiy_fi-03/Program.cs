using System.Runtime.CompilerServices;
using System.Text.RegularExpressions;
using Newtonsoft.Json;

class Lab
{
    static HashSet<char> AlphabetWithoutSpace = new HashSet<char>("абвгдежзийклмнопрстуфхцчшщыьэюя".ToCharArray());
    static HashSet<char> AlphabetWithSpace = new HashSet<char>("абвгдежзийклмнопрстуфхцчшщыьэюя ".ToCharArray());

    static string ClearText(string text, bool isSpaces)
    {
        if (isSpaces)
        {
            string clearedText = new string(text.Where(c => AlphabetWithSpace.Contains(c)).ToArray());
            clearedText = Regex.Replace(clearedText, @"\s+", " ");
            return clearedText;
        }
        else
        {
            string clearedText = new string(text.Where(c => AlphabetWithoutSpace.Contains(c)).ToArray());
            return clearedText;
        }
    }


    static string FileReader(string path)
    {
        return File.ReadAllText(path);
    }


    static Dictionary<char, int> CountLetterFrequencies(string text)
    {
        Dictionary<char, int> letterFrequencies = new Dictionary<char, int>();

        foreach (char letter in text)
        {
            if (letterFrequencies.ContainsKey(letter))
            {
                letterFrequencies[letter]++;
            }
            else
            {
                letterFrequencies[letter] = 1;
            }
        }
        return letterFrequencies.OrderByDescending(x => x.Value).ToDictionary(x => x.Key, x => x.Value);

    }


    static Dictionary<string, int> CountBigramFrequencies(string text, bool isCrossing)
    {
        if (isCrossing) return BigramWithCrossing(text);
        else return BigramWithoutCrossing(text);
    }


    static Dictionary<string, int> BigramWithCrossing(string text)
    {
        Dictionary<string, int> bigramFrequencies = new Dictionary<string, int>();

        for (int i = 0; i < text.Length - 1; i++)
        {
            var bigram = text.Substring(i, 2);

            if (bigramFrequencies.Keys.Contains(bigram))
            {
                bigramFrequencies[bigram]++;
            }
            else
            {
                bigramFrequencies[bigram] = 1;
            }
        }

        return bigramFrequencies.OrderByDescending(x => x.Value).ToDictionary(x => x.Key, x => x.Value);
    }

    static Dictionary<string, int> BigramWithoutCrossing(string text)
    {
        Dictionary<string, int> bigramFrequencies = new Dictionary<string, int>();

        for (int i = 0; i < text.Length - 1; i++)
        {
            var bigram = text.Substring(i, 2);

            if (bigramFrequencies.Keys.Contains(bigram))
            {
                bigramFrequencies[bigram]++;
            }
            else
            {
                bigramFrequencies[bigram] = 1;
            }

            i++;
        }
        return bigramFrequencies.OrderByDescending(x => x.Value).ToDictionary(x => x.Key, x => x.Value);
    }


    static double[] CountEntropy(Dictionary<char, int> letterFrequencies, Dictionary<string, int> bigramFrequencies)
    {
        long totalLetters = letterFrequencies.Values.Sum();
        double H1 = 0;
        foreach (var pair in letterFrequencies)
        {
            double p = (double)pair.Value / totalLetters;
            H1 -= p * Math.Log(p, 2);
        }

        int totalBigrams = bigramFrequencies.Values.Sum();


        double H2 = 0;
        foreach (var pair in bigramFrequencies)
        {
            double p = (double)pair.Value / totalBigrams;
            H2 -= p * Math.Log(p, 2) / 2;
        }
        return new double[] { H1, H2 };
    }


    static void CreateResultFile(string directoryPath)
    {
        string path = "results.txt";

        FileStream stream = File.Create(directoryPath + path);
        stream.Close();
    }


    static void WriteResults(string text, string path)
    {
        using (StreamWriter writer = new StreamWriter(path, true))
        {
            writer.WriteLine(text + '\n');
        }
    }


    static string FindDirectoryPath([CallerFilePath] string filePath = "")
    {
        return Path.GetDirectoryName(filePath) + '\\';
    }


    static void TextInputWithSpaces(string resultPath, string text)
    {
        WriteResults("Без перетину, але з пробілами", resultPath);
        var clearText = ClearText(text, true);
        Dictionary<char, int> letterFrequencies = CountLetterFrequencies(clearText);
        Dictionary<string, int> bigramFrequencies = CountBigramFrequencies(clearText, false);
        double[] entropy = CountEntropy(letterFrequencies, bigramFrequencies);

        string jsonLetterFreq = JsonConvert.SerializeObject(letterFrequencies);
        WriteResults(jsonLetterFreq, resultPath);

        string jsonBigramFreq = JsonConvert.SerializeObject(bigramFrequencies);
        WriteResults(jsonBigramFreq, resultPath);

        WriteResults("H1: " + entropy[0], resultPath);
        WriteResults("H2: " + entropy[1], resultPath);

    }

    static void TextInputWithSpacesAndCrossing(string resultPath, string text)
    {
        WriteResults("З перетином і пробілами", resultPath);
        var clearText = ClearText(text, true);
        Dictionary<char, int> letterFrequencies = CountLetterFrequencies(clearText);
        Dictionary<string, int> bigramFrequencies = CountBigramFrequencies(clearText, true);
        double[] entropy = CountEntropy(letterFrequencies, bigramFrequencies);

        string jsonLetterFreq = JsonConvert.SerializeObject(letterFrequencies);
        WriteResults(jsonLetterFreq, resultPath);

        string jsonBigramFreq = JsonConvert.SerializeObject(bigramFrequencies);
        WriteResults(jsonBigramFreq, resultPath);

        WriteResults("H1: " + entropy[0], resultPath);
        WriteResults("H2: " + entropy[1], resultPath);
    }

    static void TextInputWithCrossing(string resultPath, string text)
    {
        WriteResults("З перетином, але без пробілів", resultPath);
        var clearText = ClearText(text, false);
        Dictionary<char, int> letterFrequencies = CountLetterFrequencies(clearText);
        Dictionary<string, int> bigramFrequencies = CountBigramFrequencies(clearText, true);
        double[] entropy = CountEntropy(letterFrequencies, bigramFrequencies);

        string jsonLetterFreq = JsonConvert.SerializeObject(letterFrequencies);
        WriteResults(jsonLetterFreq, resultPath);

        string jsonBigramFreq = JsonConvert.SerializeObject(bigramFrequencies);
        WriteResults(jsonBigramFreq, resultPath);

        WriteResults("H1: " + entropy[0], resultPath);
        WriteResults("H2: " + entropy[1], resultPath);
    }

    static void TextInputWithoutSpacesAndCrosing(string resultPath, string text)
    {
        WriteResults("Без перетину та пробілів", resultPath);
        var clearText = ClearText(text, false);
        Dictionary<char, int> letterFrequencies = CountLetterFrequencies(clearText);
        Dictionary<string, int> bigramFrequencies = CountBigramFrequencies(clearText, false);
        double[] entropy = CountEntropy(letterFrequencies, bigramFrequencies);

        string jsonLetterFreq = JsonConvert.SerializeObject(letterFrequencies);
        WriteResults(jsonLetterFreq, resultPath);

        string jsonBigramFreq = JsonConvert.SerializeObject(bigramFrequencies);
        WriteResults(jsonBigramFreq, resultPath);

        WriteResults("H1: " + entropy[0], resultPath);
        WriteResults("H2: " + entropy[1], resultPath);
    }

    public static void run()
    {
        string directoryPath = FindDirectoryPath();
        CreateResultFile(directoryPath);
        var resultPath = directoryPath + "results.txt";
        var inputText = FileReader(directoryPath + "prestuplenie-i-nakazanie.txt");

        TextInputWithCrossing(resultPath, inputText);
        TextInputWithoutSpacesAndCrosing(resultPath, inputText);
        TextInputWithSpaces(resultPath, inputText);
        TextInputWithSpacesAndCrossing(resultPath, inputText);
    }



    class Program
    {
        static void Main(string[] args)
        {
            run();
        }
    }
}
