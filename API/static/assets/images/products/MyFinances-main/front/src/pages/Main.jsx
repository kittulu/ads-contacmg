import React from 'react';
import { Text, TextInput, ScrollView, TouchableOpacity, StyleSheet, View } from 'react-native';
import uuid from 'react-native-uuid';
import { createDrawerNavigator } from '@react-navigation/drawer';
import Finances from '../components/Finances';

const Main = ({ navigation }) => {
    const [tasks, setTasks] = React.useState([
        {
          id: uuid.v4(),
          title: 'Boleto',
          valor: '100',
        },
        {
          id: uuid.v4(),
          title: 'Pizza',
          valor: '50',
        },
    ]);

    const [title, setTitle] = React.useState([]);
    const onChangeTitle = (txtTitle) => {
      setTitle(txtTitle)
    };
    
    const [valor, setValor] = React.useState([]);
    const onChangeValor = (txtValor) => {
      setValor(txtValor)
    };
    
    // const handleTaskClick = (taskId) => {
    //     const newTasks = tasks.map((task) => {
    //       if(task.id === taskId) return { ... task, completed: !task.completed}
    //       return task;
    //     });
    
    //     setTasks(newTasks);
    // };

    const [taskUpdate, setTaskUpdate] = React.useState([]);

    const handleTaskUpdate = (taskId) => {
      const taskSelecionada = tasks.filter(task => task.id == taskId);
      
      setTitle(taskSelecionada.title)
      setValor(taskSelecionada.valor)
  
      setTaskUpdate(taskSelecionada);
    }

    const handleTaskDeletion = (taskId) => {
        const newTasks = tasks.filter(task => task.id !== taskId);
    
        setTasks(newTasks);
    }

    const onSave = () => {
        const newTasks = [... tasks,
          { 
            id: uuid.v4(),
            title: title,
            valor: valor,
          },
        ];
        
        console.log(newTasks);
        
        setTasks(newTasks);
        setTitle('')
        setValor('')
    };
    
    // const Drawer = createDrawerNavigator();

    return (  
      <ScrollView style={styles.scrollView}>
        {/* <Drawer.Navigator useLegacyImplementation initialRouteName="Finances">
            <Drawer.Screen name="Finances" component={Main}/>
            <Drawer.Screen name="Notifications" /> */}
        {/* </Drawer.Navigator> */}
        <View style={styles.container}>
          <View style={styles.form}>
            <Text style={styles.inputText}>Descricao</Text>
            <TextInput
              style={styles.input}
              keyboardType='numeric'
              onChangeText={txtTitle => onChangeTitle(txtTitle)}
              value={title}
              />
            <Text style={styles.inputText}>Valor</Text>
            <TextInput
              style={styles.input}
              onChangeText={txtValor => onChangeValor(txtValor)}
              value={valor}
            />
            <TouchableOpacity
              style={styles.button} 
              onPress={onSave}
            >
              <Text style={styles.buttonText}>Salvar</Text>
            </TouchableOpacity>
          </View>
          <View style={styles.finances}>
            <Finances 
              tasks={tasks} 
              handleTaskUpdate={handleTaskUpdate}
              handleTaskDeletion={handleTaskDeletion}/>
          </View>
        </View>
      </ScrollView>
    );
}
 
const styles = StyleSheet.create({
  scrollView: {
    backgroundColor: 'green',
  },

  container: {
      flex: 2,
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
  },

  form: {
      flex: 1,
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',

      width: 400,
      height: 200,

      borderWidth: 3,
      borderRadius: 24,
      borderColor: 'white',
      marginRight: 16,
  },

  finances: {
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'space-between',
  },

  button: {
    backgroundColor: "orange",
    borderColor: 'white',
    borderRadius:50,
    marginTop: 5,    
    marginBottom: 7,
    width: 110,
    
    height: 40,
    borderWidth: 2,
    paddingTop: 1,
    paddingLeft: 5,
  },

  buttonText: {
    textAlign: 'center',
    fontSize: 20,
    color: 'white',
  },

  input: {
    height: 40,
    borderWidth: 2,
    borderColor: 'white',
    borderRadius: 50,
    textAlign: 'center',

    color: 'white',
    fontSize: 20,
  },

  inputText: {
    color: 'white',
    fontSize: 16,
  },
});

export default Main;