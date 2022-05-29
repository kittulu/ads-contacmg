package com.unesc.myfinances.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.unesc.myfinances.entities.Usuario;
import com.unesc.myfinances.repositories.UsuarioRepository;

@Service
public class UsuarioService {

	@Autowired
	private UsuarioRepository usuRepo;
	
	@Transactional(readOnly = true)
	public void save(Usuario usuario) {
		usuRepo.save(usuario);
	}
	
	@Transactional(readOnly = true)
	public Usuario getById(Long id) {
		Usuario usuario = usuRepo.getById(id);
		return usuario;
	}
	
	@Transactional(readOnly = true)
	public List<Usuario> findAll() {
		List<Usuario> usuarioList = usuRepo.findAll(); 
		return usuarioList;
	}
}
