import React, { StyleSheet, Text, View } from 'react-native';

const Finance = ({ task, handleTaskDeletion, handleTaskUpdate }) => {
    return (  
        <View style={stylesTask.container}>
            <Text 
                style={stylesTask.text}
                onPress={() => handleTaskDeletion(task.id)}
                // onLongPress={() => handleTaskDeletion(task.id)}
              >
                {task.title}
                    <Text> --- </Text>
                R${task.valor}
            </Text>
        </View>
    );
}

const stylesTask = StyleSheet.create({
    container: {
        backgroundColor: 'gray',
        margin: 8,
        padding: 15,
        textAlign: 'end',
    },
    text:{
        fontSize: 24,
        color: 'white',
    }
});

export default Finance;