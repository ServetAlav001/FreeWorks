import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class AnaEkran extends JFrame {


    private JPanel Panel1;
    private JTextField textField1;
    private JTextField textField2;
    private JButton button1;

    public AnaEkran() {
        add(Panel1);
        setSize(500,500);
        setTitle("first Swing");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        button1.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String ad,soyad;
                ad=textField1.getText();
                soyad=textField2.getText();
                System.out.println("ad: " + ad);
                System.out.println("soyad: " + soyad);

            }
        });
    }
}
