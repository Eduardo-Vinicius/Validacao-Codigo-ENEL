using System;

namespace custo
{
    class Program
    {
        static string VerifiCusto(string cs){
            string custo = cs.Substring(88,7);
            string cdecimal = "0." + custo.Substring(5,2);
            string cvalor = custo.Substring(0,5);
            decimal ct = (Convert.ToDecimal(cvalor) + Convert.ToDecimal(cdecimal));
            if(ct <= 0)
                custo = "custo não está correto";
            else
                custo = "custo correto";
            return custo;
        }
        static void Main(string[] args)
        {
            string linha = "00000348340483300100051Bloco 1A apto 44    ##SSP29Março     20211544230007A16894030000840001550";
            Console.WriteLine(VerifiCusto(linha));
        }
    }
}
