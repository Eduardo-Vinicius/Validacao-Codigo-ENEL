using System;
using System.Linq;

 class Program
{
    static string Validaregiao(string texto)
    {
        string reg = texto.Substring(43,5);
       
            
        return reg;
    }
    static void regiao(string[] args)
    {
        string linha = "00000348340483300100051Bloco 1A apto 44    ##SSP29Março     20211544230007A16894030000840001550";
        Console.WriteLine(Validaregiao(linha));
    }
}