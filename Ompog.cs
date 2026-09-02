using System;
using System.Collections.Generic;
using System.Linq;

class NFA_Comments
{
    static void Main()
    {
        Console.OutputEncoding = System.Text.Encoding.UTF8;

        while (true)
        {
            Console.Clear();
            Console.WriteLine("==================================================");
            Console.WriteLine("      NFA C-STYLE COMMENT RECOGNIZER");
            Console.WriteLine("==================================================");
            Console.WriteLine("Sigma (Valid Alphabets):");
            Console.WriteLine("  • 'B' (Letters / Body content)");
            Console.WriteLine("  • '*'");
            Console.WriteLine("  • '/'");
            Console.WriteLine("--------------------------------------------------");
            Console.Write("Enter input (or type '0' to exit): ");

            string input = Console.ReadLine();

            if (input == "0")
            {
                Console.WriteLine("\nExiting program... Goodbye!");
                break;
            }

            // Track all possible state paths concurrently
            List<List<int>> currentPaths = new List<List<int>> { new List<int> { 0 } };

            foreach (char ch in input)
            {
                char symbol = GetSymbol(ch);
                List<List<int>> nextPaths = new List<List<int>>();

                foreach (var path in currentPaths)
                {
                    int currentState = path.Last();
                    List<int> possibleNextStates = GetNextStates(currentState, symbol);

                    // If possibleNextStates is empty (like in q5), path dies (empty set Ø)
                    foreach (int nextState in possibleNextStates)
                    {
                        List<int> newPath = new List<int>(path) { nextState };
                        nextPaths.Add(newPath);
                    }
                }

                currentPaths = nextPaths;
            }

            // Display all evaluated execution paths
            Console.WriteLine("\n--- All Possible Execution Paths ---");
            List<int> acceptedPathIndex = new List<int>();

            if (currentPaths.Count == 0)
            {
                Console.WriteLine("No active paths remaining (all paths hit empty set Ø).");
            }

            for (int i = 0; i < currentPaths.Count; i++)
            {
                var path = currentPaths[i];
                bool pathAccepted = path.Last() == 5;
                string chain = string.Join(" > ", path.Select(s => $"q{s}"));

                if (pathAccepted)
                {
                    acceptedPathIndex.Add(i + 1);
                    Console.ForegroundColor = ConsoleColor.Green;
                    Console.WriteLine($"Path {i + 1}: {chain}  --> [ACCEPTED 🟢]");
                }
                else
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine($"Path {i + 1}: {chain}  --> [REJECTED 🔴]");
                }
                Console.ResetColor();
            }

            // Final Conclusion
            Console.WriteLine("\n--------------------------------------------------");
            if (acceptedPathIndex.Count > 0)
            {
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine($"🟢 OVERALL RESULT: ACCEPTED");
                Console.WriteLine($"Conclusion: The NFA accepts the input using Path {string.Join(", ", acceptedPathIndex)}.");
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine($"🔴 OVERALL RESULT: REJECTED");
                Console.WriteLine("Conclusion: None of the available execution paths reached the accept state (q5).");
            }
            Console.ResetColor();
            Console.WriteLine("--------------------------------------------------");

            Console.WriteLine("\nPress ENTER to test another input...");
            Console.ReadLine();
        }
    }

    // Directly matches the delta functions & transition table from your written paper
    static List<int> GetNextStates(int state, char symbol)
    {
        List<int> next = new List<int>();

        switch (state)
        {
            case 0: // q0
                if (symbol == '/') next.Add(1);      // δ(q0, /) = {q1}
                else next.Add(4);                   // δ(q0, B/*) = {q4}
                break;

            case 1: // q1
                if (symbol == '*') next.Add(2);      // δ(q1, *) = {q2}
                else next.Add(4);                   // δ(q1, B//) = {q4}
                break;

            case 2: // q2
                if (symbol == 'B' || symbol == '/') next.Add(2); // δ(q2, B) = {q2}, δ(q2, /) = {q2}
                if (symbol == '*')
                {
                    next.Add(3);                     // δ(q2, *) = {q3, q4}
                    next.Add(4);
                }
                break;

            case 3: // q3
                if (symbol == 'B')
                {
                    next.Add(2);                     // δ(q3, B) = {q2, q4}
                    next.Add(4);
                }
                if (symbol == '*')
                {
                    next.Add(3);                     // δ(q3, *) = {q3, q4}
                    next.Add(4);
                }
                if (symbol == '/') next.Add(5);      // δ(q3, /) = {q5}
                break;

            case 4: // q4 (Trap State)
                next.Add(4);                         // δ(q4, x) = {q4}
                break;

            case 5: // q5 (Accept State - No transitions per paper Ø)
                // δ(q5, x) = Ø (No next states added)
                break;
        }

        return next;
    }

    static char GetSymbol(char ch)
    {
        if (ch == '*') return '*';
        if (ch == '/') return '/';
        return 'B'; // Treats all letters & other symbols as 'B'
    }
}