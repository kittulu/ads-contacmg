package com.unesc.myfinances.entities;

import java.time.LocalDate;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.ForeignKey;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.Table;

import lombok.Data;

@Data
@Entity
@Table(name = "usuario")
public class Usuario {
	
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	@Column(name = "usu_id")
	private Long id;
	
	@ManyToOne
	@JoinColumn(name = "sit_id",  foreignKey = @ForeignKey(name = "fk_usuario_situacao"))
	private Situacao situacao;
	
	@Column(name = "usu_login", nullable = false, length = 30, unique = true)
	private String login;
	
	@Column(name = "usu_senha", nullable = false, length = 120, unique = false)
	private String senha;
	
	@Column(name = "usu_dataCadastro", nullable = true, length = 120, unique = false)
	private LocalDate dataCadastro;
	
	@Column(name = "usu_email", nullable = true, length = 120, unique = true)
	private String email;

	@Column(name = "usu_apelido", nullable = true, length = 70, unique = false)
	private String apelido;
}
