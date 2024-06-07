module com.example.multiples {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.multiples to javafx.fxml;
    exports com.example.multiples;
}