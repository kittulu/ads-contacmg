package com.unesc.myfinances.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.transaction.annotation.Transactional;

import com.unesc.myfinances.entities.Situacao;
import com.unesc.myfinances.repositories.SituacaoRepository;

public class SituacaoService {

	@Autowired
	private SituacaoRepository sitRepo;
	
	@Transactional(readOnly = true)
	public void save(Situacao situacao) {
		sitRepo.save(situacao);
	}
	
	@Transactional(readOnly = true)
	public Situacao getById(Long id) {
		Situacao situacao = sitRepo.getById(id);
		return situacao;
	}
	
	@Transactional(readOnly = true)
	public List<Situacao> findAll() {
		List<Situacao> situacaoList = sitRepo.findAll(); 
		return situacaoList;
	}
}
