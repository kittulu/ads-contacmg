package com.unesc.myfinances.entities;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

import lombok.Data;

@Data
@Entity
@Table(name = "financesTipo")
public class FinancesTipo {
	
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	@Column(name = "fint_id")
	private Long id;

	@Column(name = "fint_descricao", nullable = false, length = 120, unique = false)
	private String descricao;

	@Column(name = "fint_tag", nullable = false, length = 120, unique = false)
	private String tag;
}
