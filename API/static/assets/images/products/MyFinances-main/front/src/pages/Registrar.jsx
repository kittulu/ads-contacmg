import React from 'react';
import { StyleSheet, Text, View, TextInput, TouchableOpacity, assets} from 'react-native';


const Registrar = ({ navigation }) => {
    return (  
    <View style={styles.container}>
        <Text
          style={styles.forms}
          >Nome
        </Text>

        <TextInput
          style={styles.input}
          placeholder="Nome"
        />

        <Text
            style={styles.forms}
            > Sobrenome
        </Text>

        <TextInput
            style={styles.input}
            placeholder="Sobrenome"
        />

        <Text
            style={styles.forms}
            >Gmail
        </Text>

        <TextInput
            style={styles.input}
            placeholder="Gmail"
        />

        <Text
            style={styles.forms}
            >Senha
        </Text>

        <TextInput
            style={styles.input}
            returnKeyLabel="Senha"
            placeholder="Senha"
        />
        
        <Text
            style={styles.forms}
            >Repita a Senha
        </Text>
        
        <TextInput
            style={styles.input}
            returnKeyLabel="Repita Sua Senha"
            placeholder="Repita Sua Senha"
        />
        
        <TouchableOpacity
            style={styles.button}
            onPress={() => navigation.navigate('Login')}
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
      marginTop: 18,    
      width: 110,
  
      textAlign: 'center',
      height: 40,
      paddingTop: 4,
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

export default Registrar;