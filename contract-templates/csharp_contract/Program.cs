using System;
using System.Text;
using Contract;

namespace root
{
    class Program
    {
        static void Main(string[] args)
        {
            string buffer = Console.In.ReadToEnd();
            ContractHandler c = new ContractHandler();

            string responseValue = c.Handle(buffer);

            if(responseValue != null) {
                Console.Write(responseValue);
            }
        }
    }
}
