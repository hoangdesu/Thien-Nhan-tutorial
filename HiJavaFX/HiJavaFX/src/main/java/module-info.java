module com.hijavafx {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.hijavafx to javafx.fxml;
    exports com.hijavafx;
}