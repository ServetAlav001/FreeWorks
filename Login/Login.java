import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Login extends JFrame{
    private JPanel panel1;
    private JTextField KullaniciText;
    private JTextField sifreText;
    private JButton Giris;
public Login() {
    add(panel1);
    setSize(500,500);
    setTitle("login");

    Giris.addActionListener(new ActionListener() {
        @Override
        public void actionPerformed(ActionEvent e) {
            String kullanici_Adi = KullaniciText.getText();
            String Sifre =sifreText.getText();
            String message=null;
            if(kullanici_Adi.equals("servet alav") && Sifre.equals("12345")){
                message ="hosgeldiniz..";
                JOptionPane.showMessageDialog(panel1,message);
                System.exit(0);
                setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

            } else if (!kullanici_Adi.equals("servet alav") || !Sifre.equals("12345")) {
                message = "kullanici adi veya parola hatali";
                JOptionPane.showMessageDialog(panel1,message);
            }
            KullaniciText.setText("");
            sifreText.setText("");


        }
    });
}
}
