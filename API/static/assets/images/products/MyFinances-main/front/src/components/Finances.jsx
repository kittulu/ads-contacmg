import React, { StyleSheet, View } from 'react-native';
import Finance from './Finance';

const Finances = ({ tasks, handleTaskDeletion, handleTaskUpdate }) => {
    return (
        <View style={stylesTask.container}>
            {tasks.map((task) => (
                <Finance 
                    task={task} 
                    handleTaskUpdate={handleTaskUpdate}
                    handleTaskDeletion={handleTaskDeletion}
                />
            ))}
        </View>
    );
};

const stylesTask = StyleSheet.create({
    container: {
        width: 500,
        height: 250,
    },
});
 
export default Finances;