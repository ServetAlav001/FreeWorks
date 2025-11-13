import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.ComponentAdapter;

public class Arayuz extends JFrame{
    private JPanel mainPanel;
    private JButton a7Button;
    private JButton a4Button;
    private JButton a1Button;
    private JButton a0Button;
    private JButton a8Button;
    private JButton a5Button;
    private JButton a2Button;
    private JButton a9Button;
    private JButton a6Button;
    private JButton a3Button;
    private JButton esittirButton;
    private JButton artiButton;
    private JButton eksiButton;
    private JButton carpiButton;
    private JButton bolmeButton;
    private JTextField sayiText;

    private JTextField sonucText;
    private JButton temizleButton;

    //sayıları okur
    private void numaraEnter(String s){
        String no = sayiText.getText() + s;
        sayiText.setText(no);
    }
    long sayi1;
    long sayi2;
    long sonuc;
    String islem;
    public Arayuz(){
        setContentPane(mainPanel);
        setTitle("welcame");
        setSize(400,400);
        setVisible(true);
        setDefaultCloseOperation(EXIT_ON_CLOSE);

        // arayuzu temizler
        temizleButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {

                sayiText.setText("");
                sonucText.setText("");
            }
        });
        //sayıları toplar
        artiButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {

                 sayi1 = Long.parseLong(sayiText.getText());
                 sayiText.setText("");
                 islem="+";
            }
        });
        //sayıların farkını hesaplar
        eksiButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                sayi1 = Long.parseLong(sayiText.getText());
                sayiText.setText("");
                islem="-";
            }
        });
        //sayıları carpar
        carpiButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                sayi1 = Long.parseLong(sayiText.getText());
                sayiText.setText("");
                islem="*";
            }
        });
        //sayıları boler
        bolmeButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                sayi1 = Long.parseLong(sayiText.getText());
                sayiText.setText("");
                islem="/";
            }
        });
        a0Button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                numaraEnter("0");
            }
        });
        a1Button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                numaraEnter("1");
            }
        });
        a2Button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                numaraEnter("2");
            }
        });
        a3Button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                numaraEnter("3");
            }
        });
        a6Button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                numaraEnter("6");
            }
        });
        a5Button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                numaraEnter("5");
            }
        });

        a4Button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                numaraEnter("4");
            }
        });
        a7Button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                numaraEnter("7");
            }
        });
        a8Button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                numaraEnter("8");
            }
        });
        a9Button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                numaraEnter("9");
            }
        });
        //sayıların isleme gore sonucunu yazdırır
        esittirButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    sayi2 = Long.valueOf(sayiText.getText());
                    if(islem.equals("+")){
                        sonuc =  sayi1+sayi2;
                        sonucText.setText(String.valueOf(sonuc));
                    }else if(islem.equals("-")){
                        sonuc =  sayi1-sayi2;
                        sonucText.setText(String.valueOf(sonuc));
                    }else if(islem.equals("*")){
                        sonuc =  sayi1*sayi2;
                        sonucText.setText(String.valueOf(sonuc));
                    }else if(islem.equals("/")){
                        try {
                            sonuc =  sayi1/sayi2;
                            sonucText.setText(String.valueOf(sonuc));
                        }catch (ArithmeticException ex){
                            sonucText.setText(ex.getMessage());
                        }
                    }
                }catch (NumberFormatException ex){
                    sonucText.setText(ex.getMessage());
                }
            }
        });
    }
    public static void main(String[] args){
        Arayuz arayuz = new Arayuz();
    }
}
