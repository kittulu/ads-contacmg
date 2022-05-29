package com.unesc.myfinances.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.transaction.annotation.Transactional;

import com.unesc.myfinances.entities.FinancesTipo;
import com.unesc.myfinances.repositories.FinancesTipoRepository;

public class FinancesTipoService {

	@Autowired
	private FinancesTipoRepository usuRepo;
	
	@Transactional(readOnly = true)
	public void save(FinancesTipo financesTipo) {
		usuRepo.save(financesTipo);
	}
	
	@Transactional(readOnly = true)
	public FinancesTipo getById(Long id) {
		FinancesTipo financesTipo = usuRepo.getById(id);
		return financesTipo;
	}
	
	@Transactional(readOnly = true)
	public List<FinancesTipo> findAll() {
		List<FinancesTipo> financesTipoList = usuRepo.findAll(); 
		return financesTipoList;
	}
}
