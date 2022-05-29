package com.unesc.myfinances.controllers;

import java.text.ParseException;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.unesc.myfinances.dto.FinancesGetResponseDTO;
import com.unesc.myfinances.dto.FinancesPostRequestDTO;
import com.unesc.myfinances.entities.Finances;
import com.unesc.myfinances.service.FinancesService;

@RestController
@RequestMapping("/finances")
public class FinancesController {

	@Autowired
	private FinancesService finService;
	
	@GetMapping
	public ResponseEntity<List<FinancesGetResponseDTO>> list(){
		List<Finances> finList = finService.findAll();
		List<FinancesGetResponseDTO> resList = FinancesGetResponseDTO.convertList(finList);
		return ResponseEntity.ok(resList);
	}
	
	@PostMapping
	public ResponseEntity<FinancesGetResponseDTO> create(@RequestBody FinancesPostRequestDTO finDTO) throws ParseException{
		Finances finances = FinancesPostRequestDTO.convert(finDTO);
		
		finService.save(finances);
		
		return ResponseEntity.ok(FinancesGetResponseDTO.convert(finances));
	}
}
