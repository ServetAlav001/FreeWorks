import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Arayuz extends JFrame{
    private JPanel jparayuz;
    private JTextField isimText;
    private JTextField soyisimText;
    private JPasswordField sifrePassword;
    private JButton girisButton;
    private JButton temizleButton;
    private JButton kayitOlButton;
    private JLabel sonuclabel;
    private String isim;
    private String soyisim;
    private String sifre;

    public String getIsim() {
        return isim;
    }

    public void setIsim(String isim) {
        this.isim = isim;
    }

    public String getSoyisim() {
        return soyisim;
    }

    public void setSoyisim(String soyisim) {
        this.soyisim = soyisim;
    }

    public String getSifre() {
        return sifre;
    }

    public void setSifre(String sifre) {
        this.sifre = sifre;
    }

    public Arayuz(String isim, String soyisim, String sifre) {
        this.isim=isim;
        this.soyisim=soyisim;
        this.sifre=sifre;

    setTitle("Login");
    setSize(500,500);
    setDefaultCloseOperation(EXIT_ON_CLOSE);
    setVisible(true);
    setContentPane(jparayuz);

    girisButton.addActionListener(new ActionListener() {
        @Override
        public void actionPerformed(ActionEvent e) {
            try {
                if(isimText.getText().equals(isim)&&soyisimText.getText().equals(soyisim)&&sifrePassword.getText().equals(sifre)){
                    sonuclabel.setText("giris basarili");
                }
                else{
                    sonuclabel.setText("giris basarisiz.");
                }
            }catch (Exception ex){
                sonuclabel.setText(ex.getMessage());
            }
        }
    });
    kayitOlButton.addActionListener(new ActionListener() {
        @Override
        public void actionPerformed(ActionEvent e) {
            try {
                if(!isimText.getText().equals(isim)|| !soyisimText.getText().equals(soyisim)|| !sifrePassword.getText().equals(sifre)){
                    sonuclabel.setText("giris basarili");
                }
                else{
                    sonuclabel.setText("giris basarisiz. bu kullanici kayitli");
                }
            }catch (Exception ex){
                sonuclabel.setText(ex.getMessage());
            }
        }
    });
    temizleButton.addActionListener(new ActionListener() {
        @Override
        public void actionPerformed(ActionEvent e) {
            isimText.setText("");
            soyisimText.setText("");
            sifrePassword.setText("");
            sonuclabel.setText("");
        }
    });
}
}
