using System;
using System.Linq;

namespace kw
{
    class Program
    {
        static string VerificaKw(string k){
            string kw = k.Substring(82,6);
            if(!(kw.All(char.IsDigit)) || kw != "000000")
                kw = "kw okay";
            else
                kw = "kw não é valido";
            return kw;
        }
        static void Main(string[] args)
        {
            string linha = "00000348340483300100051Bloco 1A apto 44    ##SSP29Março     20211544230007A16894030000840001550";
            Console.WriteLine(VerificaKw(linha));
        }
    }
}
