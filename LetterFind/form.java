mport javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Arayuz extends JFrame{

    private JTextArea textArea1;
    private JButton Button1;
    private JTextField textField1;
    private JTextField textField2;
    private JPanel panel1;

public Arayuz() {
    add(panel1);
    setSize(500,500);
    setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);


    Button1.addActionListener(new ActionListener() {
        @Override
        public void actionPerformed(ActionEvent e) {
            String yazi = textArea1.getText();
            int kelime_sayisi=0;
            int harf_sayisi =0;
            for(int i=0;i<yazi.length();i++){
                if(yazi.charAt(i)!=' '){
                    harf_sayisi++;
                }
            }
            String[] array =yazi.split(" ");
            for (String kelime:array) {
                kelime_sayisi++;
            }
            textArea1.setText(yazi);
            textField1.setText(String.valueOf(kelime_sayisi));
            textField2.setText(String.valueOf(harf_sayisi));
        }

    });
}
}
