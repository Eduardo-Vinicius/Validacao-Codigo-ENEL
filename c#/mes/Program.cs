using System;

namespace mes
{
    class Program
    {
        static string ValidaMes(string mes){
            string month = mes.Substring(50,10);
            if(MesValido(VerificaMes(month),month)){
                month = "mês Valido";
            }
            else{
                month = "mês não é valido";
            }
            return month;
        }
        static bool MesValido(int nmes, string mes){
            if(nmes == 1){
                if(mes.Substring(7,3) == "   "){
                    return true;
                }
            }
            else if(nmes == 2){
                if(mes.Substring(9,1) == " "){
                    return true;
                }
            }
            else if(nmes == 3){
                if(mes.Substring(5,5) == "     "){
                    return true;
                }
            }
            else if(nmes == 4){
                if(mes.Substring(5,5) == "     "){
                    return true;
                }
            }
            else if(nmes == 5){
                if(mes.Substring(4,6) == "      "){
                    return true;
                }
            }
            else if(nmes == 6){
                if(mes.Substring(5,5) == "     "){
                    return true;
                }
            }
            else if(nmes == 7){
                if(mes.Substring(5,5) == "     "){
                    return true;
                }
            }
            else if(nmes == 8){
                if(mes.Substring(6,4) == "    "){
                    return true;
                }
            }
            else if(nmes == 9){
                if(mes.Substring(8,2) == "  "){
                    return true;
                }
            }
            else if(nmes == 10){
                if(mes.Substring(7,3) == "   "){
                    return true;
                }
            }
            else if(nmes == 11){
                if(mes.Substring(8,2) == "  "){
                    return true;
                }
            }
            else if(nmes == 12){
                if(mes.Substring(8,2) == "  "){
                    return true;
                }
            }
            else
                return false;
            
            return false;
        }
        static int VerificaMes(string mes){
            if(mes.Substring(0,7) == "Janeiro"){
                return 1;
            }
            else if(mes.Substring(0,9) == "Fevereiro"){
                return 2;
            }
            else if(mes.Substring(0,5) == "Março"){
                return 3;
            }
            else if(mes.Substring(0,5) == "Abril"){
                return 4;
            }
            else if(mes.Substring(0,4) == "Maio"){
                return 5;
            }
            else if(mes.Substring(0,5) == "Junho"){
                return 6;
            }
            else if(mes.Substring(0,5) == "Julho"){
                return 7;
            }
            else if(mes.Substring(0,6) == "Agosto"){
                return 8;
            }
            else if(mes.Substring(0,8) == "Setembro"){
                return 9;
            }
            else if(mes.Substring(0,7) == "Outubro"){
                return 10;
            }
            else if(mes.Substring(0,8) == "Novembro"){
                return 11;
            }
            else if(mes.Substring(0,8) == "Dezembro"){
                return 12;
            }
            else
                return 13;
        }
        static void Main(string[] args)
        {
            string texto = "00000348340483300100051Bloco 1A apto 44    ##SSP29Dezembro  20211544230007A16894030000840001550";
            Console.WriteLine(ValidaMes(texto));
        }
    }
}
