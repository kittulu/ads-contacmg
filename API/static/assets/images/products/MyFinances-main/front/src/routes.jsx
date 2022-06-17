import * as React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import Main from './pages/Main';
import Login from './pages/Login';
import Registrar from './pages/Registrar';
import Home from './pages/Home';

const Stack = createNativeStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen
          name="Login"
          component={Login}
          options={{ title: 'Login' }}
        />
        <Stack.Screen
          name="Registrar"
          component={Registrar}
          options={{ title: 'Registrar-se' }}
        />
        <Stack.Screen
          name="Home"
          component={Main}
          options={{ title: 'Finances' }}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
};