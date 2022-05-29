import React from 'react';
import { StyleSheet, Text, View, TextInput, TouchableOpacity, assets} from 'react-native';


const Login = ({ navigation }) => {
    return (  
    <View style={styles.container}>
        <Text
            style={styles.forms}
        >Gmail
        </Text>
        <TextInput
            style={styles.input}
            placeholder="Digite Seu Usuario"
        />
        <Text
            style={styles.forms}
        >Senha
        </Text>
        <TextInput
            secureTextEntry={true}
            style={styles.input}
            placeholder="Digite Sua Senha"
        />
        <TouchableOpacity
            style={styles.button}
            onPress={() => navigation.navigate('Home')}
        >Entrar
        </TouchableOpacity>
        <TouchableOpacity
            style={styles.button}
            onPress={() => navigation.navigate('Registrar')}
        >Registrar
        </TouchableOpacity>
    </View>
    );
}

const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: 'green',
      alignItems: 'center',
      justifyContent: 'center',
    },
  
    button: {
      backgroundColor: "orange",
      borderColor: 'white',
      borderRadius:50,
      marginTop: 5,    
      width: 110,
  
      textAlign: 'center',
      height: 40,
      paddingTop: 2,
      borderWidth:2,
      paddingTop:5,
      paddingLeft: 5,
      textAlign:'center',
  
      fontSize: 20,
      color: 'white',
  
    },
    input: {
      height: 40,
      borderColor: 'red',
      borderWidth: 2,
      borderColor: 'white',
      borderRadius: 50,
      textAlign: 'center',
  
      placeholderTextColor: 'white',
    },
});

export default Login;