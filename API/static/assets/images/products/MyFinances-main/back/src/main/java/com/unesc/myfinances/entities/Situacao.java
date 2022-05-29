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
@Table(name = "situacao")
public class Situacao {

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	@Column(name = "fin_id")
	private Long id;

	@Column(name = "sit_descricao", nullable = false, length = 120, unique = false)
	private String descricao;
	
	@Column(name = "sit_tag", nullable = false, length = 120, unique = false)
	private String tag;
}
